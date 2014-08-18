/* =========================================================================
 * This file is part of mt-c++ 
 * =========================================================================
 * 
 * (C) Copyright 2004 - 2009, General Dynamics - Advanced Information Systems
 *
 * mt-c++ is free software; you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public 
 * License along with this program; If not, 
 * see <http://www.gnu.org/licenses/>.
 *
 */

#include <mt/ThreadPosix.h>

#if defined(HAVE_PTHREAD_H)

#ifdef WIN32
#   define SIGKILL 0
#endif
void mt::ThreadPosix::start()
{

    if (getLevel() != DEFAULT_LEVEL)
    {
        throw mt::ThreadResourceException("Cannot determine upfront wheteher pthread threads are implemented using kernel or user level threads.  Set the level to DEFAULT_LEVEL");
    }

    if (getPriority() != NORMAL_PRIORITY)
    {
        sched_param sp;

        if (getPriority() == MAXIMUM_PRIORITY)
            sp.sched_priority = sched_get_priority_max(SCHED_OTHER);

        else if (getPriority() == MINIMUM_PRIORITY)
            sp.sched_priority = sched_get_priority_min(SCHED_OTHER);

        pthread_attr_t attr;
        pthread_attr_init(&attr);
        pthread_attr_setschedparam(&attr,
                                   &sp);

        if (::pthread_create(&mNative,
                             &attr,
                             (void *(*)(void *))this->__start,
                             this) != 0)
            throw mt::ThreadResourceException("pthread_create()");
        pthread_attr_destroy(&attr);
    }
    else
    {
        if (::pthread_create(&mNative,
                             NULL,
                             (void *(*)(void *))this->__start,
                             this) != 0)
            throw mt::ThreadResourceException("pthread_create()");
    }
}
void *mt::ThreadPosix::__start(void *v)
{
    STANDARD_START_CALL(ThreadPosix, v);
    /*
    mt::Runnable *runnable = 
        static_cast<mt::Runnable *>(v);

    runnable->run();

    // If the pointers don't match, then the runnable is not 'this'
    // and therefore it's ok to delete the runnable.
    delete runnable;
    */

    pthread_exit(NULL);
    return NULL;
}

void mt::ThreadPosix::kill()
{
    if (pthread_kill(mNative, SIGKILL) != 0)
    {
        throw mt::ThreadResourceException("pthread_kill()");
    }
    setIsRunning(false);
}
void mt::ThreadPosix::join()
{
    if (::pthread_join(mNative, NULL) != 0)
        throw mt::ThreadResourceException("pthread_join()");
}
void mt::ThreadPosix::yield()
{
    ::sched_yield();
}

#endif
